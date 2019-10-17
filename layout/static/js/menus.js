// Use focus-within polyfill so no having to maintain where the current focus is within tree
// Let the DOM do it!
// https://github.com/matteobad/focus-within-polyfill

/**

The following code expects you to have the following layout style for your list and sub-lists
This allows us to generate all the meta-data we need to have in order to move through the list
using the keyboard

+---+-------------------+
|li | List item index 0 |
+-----------------------+
|li | List item index 1 |
+---+--+----------------+
   |ul | Un-ordered list|
   +-+-+--+----------------------+
     | li | Sub-list item index 0|
     +---------------------------+
     | li | Sub-list item index 1|
     +----+--+-------------------+
         |ul | Un-ordered list|
         +---+--+--------------------------+
            |li | Sub-sub-list item index 0|
            +---+--------------------------+

*/

/**
 * This function will provide information about the grand-parent, the parent index, etc.
 * It's meant to be ran on a UL that has a parent LI that contains a listitem
 * @param {*} parentUlEl - A UL element
 */
const getUlMetaData = parentUlEl => {
	const parentLiEl = parentUlEl.parentElement.tagName === 'LI' && parentUlEl.parentElement; // If false, is root
	const strParentIndex = parentLiEl && parentLiEl.dataset.menuindex; // If false, is root
	const parentIndex = Number(strParentIndex);
	const grandParentUlEl = parentLiEl && parentLiEl.parentElement; // If false, is root
	const isRoot = !parentLiEl || !grandParentUlEl;

	return {
		parentLiEl,
		parentIndex,
		grandParentUlEl,
		isRoot,
	};
};

document.addEventListener('DOMContentLoaded', () => {
	const menuGroups = Array.from(document.querySelectorAll('.dropdown-menu-list'));

	menuGroups.forEach(menuGroupUlEl => {
		const menuLiItems = Array.from(menuGroupUlEl.children);
		const parentUlEl = menuGroupUlEl;

		const { parentIndex, grandParentUlEl } = getUlMetaData(parentUlEl);

		menuLiItems.forEach((menuLiElement, strMenuIndex) => {
			const menuIndex = Number(strMenuIndex);
			menuLiElement.setAttribute('data-menuindex', menuIndex);

			const getMenuItemByI = (j, el) =>
				Array.from(el.children).find(child => Number(child.dataset.menuindex) === Number(j));

			menuLiElement.addEventListener('keydown', e => {
				const stop = () => {
					e.stopPropagation();
					e.preventDefault();
				};

				switch (e.key) {
					case 'ArrowDown': {
						// Get the item below the current one
						// If nothing is there, go ahead and get the parent one after the current parent
						stop();
						let el = getMenuItemByI(menuIndex + 1, parentUlEl);
						// If overflowing to the parent item below

						let ul = parentUlEl;
						if (!el && ul) {
							/**               
                The following while loop solves for the following scenario when trying to use
                the down arrow to go from sub-sub list item 0 to list item 1 where we need to
                traverse up the tree in order to find the parent index

                +---+-------------------+
                |li | List item index 0 |
                +---+--+----------------+
                  |ul | Un-ordered list|
                  +-+-+--+----------------------+
                    | li | Sub-list item index 0|
                    +---------------------------+
                    | li | Sub-list item index 1|
                    +----+--+-------------------+
                        |ul | Un-ordered list|
                        +---+--+--------------------------+
                            |li | Sub-sub-list item index 0|
                +---+-----------+-------+------------------+
                |li | List item index 1 |
                +---+-------------------+
               */
							while (true) {
								const {
									parentIndex: gpIndex,
									grandParentUlEl: newGrandParentUlEl,
									isRoot,
                } = getUlMetaData(ul);
                // See if an element matches what's supposed to be below
                const tmpEl = getMenuItemByI(gpIndex + 1, newGrandParentUlEl);
                // If there is, set that as the element to focus on and return
								if (el || tmpEl) {
									el = tmpEl;
									break;
                }
                // Otherwise, if it's root there's no reason to continue through the while loop
                if (isRoot) break;
                // Set ul for the new iteration up the UL tree
								ul = newGrandParentUlEl;
							}
						}
						// T'was root, and there was no item lower, let's return
						if (!el) break;
						el.focus();
						break;
					}
					case 'ArrowUp': {
						stop();
						// If overflows, select menu below submenu
						let el = getMenuItemByI(menuIndex - 1, parentUlEl);
						if (!el && grandParentUlEl)
							el =
								menuIndex == 0
									? getMenuItemByI(parentIndex, grandParentUlEl)
									: getMenuItemByI(parentIndex - 1, grandParentUlEl);
						if (!el) break;
						el.focus();
						break;
					}
					case 'Enter':
					case ' ':
						stop();
						// Fall thru intentionally - make sure that right arrow isn't just clicking
						if (!menuLiElement.dataset.haschildren) menuLiElement.children[0].click();
					case 'ArrowRight':
						stop();
						if (!menuLiElement.dataset.haschildren) break;
						const el = Array.from(
							Array.from(menuLiElement.children).find(child => child.tagName === 'UL').children
						)[0];
						if (!el) break;
						el.focus();
						break;
					case 'ArrowLeft': // Thing
						// If root, don't do anything
						if (!grandParentUlEl) break;
						stop();
						getMenuItemByI(parentIndex, grandParentUlEl).focus();
						break;
					default:
						break;
				}
			});
		});
	});
});

Project Structure
=================

This section covers general pattoo-web file structure. Due to the project being
based in Reactjs, a javascript framework, the file structure is pretty
opiniated. A pragmatic approach to structing the project was followed, in which
groups of related elements/components were placed placed together.

It should also be noted that following JavaScript testing convention unittests
for even elements are co-located with the given element/component.

Project Root
------------

.. code-block:: bash

    ├── docs
    ├── .eslintrc.json
    ├── .git
    ├── .github
    ├── .gitignore
    ├── jsconfig.json
    ├── LICENSE
    ├── package.json
    ├── package-lock.json
    ├── postcss.config.js
    ├── public
    ├── README.rst
    ├── .readthedocs.yml
    ├── setup
    ├── src
    ├── tailwind.config.js
    ├── tailwind-default.config.js
    └── .travis.yml

Key Project Configuration Files
-------------------------------

* jsconfig.json: Primarly allows for setting project root directory, and allows
  for absolute path imports anywhere in the `src` folder.
* postcss.config.js
* tailwind.config.js
* tailwind-default.config.js
* .eslintrc.json

Source Folder (src)
-------------------

The goal for the source folders is to keep the project from having a `depth
heavy` file structure.

.. code-block:: bash

    src
    ├── assets
    ├── components
    │   └── sidebar
    │       └── components
    ├── routes
    │   ├── base
    │   ├── dashboard
    │   ├── login
    │   └── routeClient
    ├── styles
    └── utils
        ├── api
        └── query

* `assets` holds all images and icons used througout the project
* `components` stores all project
* `routes` stores all page application pages, these operate like components as
  well, but a large component with smaller developer defined components or
  third-party components.
* `routeClient` this is not a page route, but this handles routing within the
  application, this is where all routes in the `routes` folder is registered.
* `styles` stores compiled tailwindcss styles
* `utils` stores applicaiton buinsess logic that is not related to styled
  components.

General rule of thumb is to place reusable components within the components
folder. In the case of a component that can only be utilized within one
component, you can create an additional sub-component directory within the
parent component that houses components that can be utilized within the parent
component.

e.g The `sidebar` component has a sub-directory that contains additional
components only usable or applicable in the `sidebar` component.

Javascript Module Structure
---------------------------

.. code-block:: bash

    routeClient
    ├── index.js
    ├── routesClient.css
    ├── routesClient.js
    └── routesClient.test.js

* `index.js` this is used to export the default and named exports from a given
  module.
* `routeClient.js` this houses the actual code for a given module, additional
  module files ot separate concern is advise so as to not have large files.
* `routesClient.test.js` this file tests the various elements within the
  `routesClient.js`, this convention of using `filename.test.js` should be used
  throughout to test each module file.

Additional Notes
----------------

* Try to utilize absolute imports, this is convention that is used throughout
  the other `pattoo` projects and would be greatly be advise to mirror this
  convention for `pattoo-web`. This is achieved through the `jsconfig.json` file
  which denotes the root of the project and the `source folder (src)`
* Do not create project folders that are more than three levels in depth. This
  is so that when importing a given module that the filepaths are not very long,
  and much easier to find varioius files when needed.

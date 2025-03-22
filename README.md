# Ricebowl

Ricebowl is a tool created in order to streamline the process of installing other user's rices, or publishing your own!

## Usage

### Installing a Rice

- To see available rices in the [repo](https://github.com/StikyPiston/ricebowl-repo), run `ricebowl-cli list`
- When you find one you like, run `ricebowl-cli install [rice name]` to install it!

### Publishing a rice

- To publish a rice, you must first place the files onto a public Git repo, such as GitHub.
- Then, at the root of your repo, create a `bowl.json` file.
- Inside, put the properties of it, dependencies, and an index of file locations.
- For an example, see [this repo](https://github.com/stikypiston/darkroast-bspwm)
- Then, once ready, create a Pull Request on *this* repo, and add your repo's details into the repo.json file.
- See the other rices for how to do so.
- If the PR is accepted, your rice will be successfully published!

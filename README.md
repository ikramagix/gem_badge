# GEM_BADGE

GEM_BADGE is a lightweight tool that allows you to showcase the download count of your Ruby gem directly on your GitHub README. By leveraging dynamic Shields.io badges, GEM_BADGE provides a quick and easy way to visually represent your gem's popularity.

## Features
- Fetches total download counts from [RubyGems.org](https://rubygems.org/).
- Generates a dynamic badge compatible with Shields.io.
- Simple and intuitive setup for any Ruby gem.

## Usage
1. Deploy GEM_BADGE on your preferred platform (e.g., Render, Railway).
2. Replace `<gem_name>` in the badge URL with your gem's name:
   ```markdown
   ![Downloads](https://example.com/downloads/<gem_name>)
   ```
3. Add the badge to your GitHub README to display the download count.

## Example
For a gem named `faussaire`, the badge URL would look like this:
```markdown
![Downloads](https://example.com/downloads/faussaire)
```

This would render as:
![Downloads](https://img.shields.io/endpoint?url=https://gem-badge.onrender.com/downloads/faussaire)

## License
GEM_BADGE is distributed under the [CC BY-NC 4.0 License](LICENSE.txt).
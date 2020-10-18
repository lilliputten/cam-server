/** @module config-overrides
 *  @since 2020.10.18, 21:16
 *  @changed 2020.10.18, 21:16
 */

/* eslint-env es6, node, commonjs */
// const rewireTypescript = require('react-app-rewire-typescript');
const rewirePostcss = require('react-app-rewire-postcss');

const

  path = require('path'),

  srcRoot = process.cwd(),
  prjRoot = srcRoot.replace(/\\/g, '/'),

  configCss = {}, // require('./src/config/__css/config__css'),

  /** postcssPlugins ** {{{ */
  postcssPlugins = [
    require('postcss-import'),
    require('postcss-mixins')({
      mixinsDir: path.join(prjRoot, 'src', 'blocks', '!mixins'),
    }), // https://github.com/postcss/postcss-mixins
    require('postcss-random'), // https://www.npmjs.com/package/postcss-random
    require('postcss-each'),
    require('postcss-for'),
    require('postcss-define-function'), // https://github.com/titancat/postcss-define-function
    require('postcss-advanced-variables')({ // https://github.com/jonathantneal/postcss-advanced-variables
      // unresolved: 'warn', // 'ignore',
      variables: configCss,
    }),
    require('postcss-simple-vars'), // https://github.com/postcss/postcss-simple-vars
    require('postcss-conditionals'), // Already used (scss?)
    require('postcss-color-function'), // https://github.com/postcss/postcss-color-function
    require('postcss-calc')(),
    require('postcss-nested-ancestors'), // https://github.com/toomuchdesign/postcss-nested-ancestors
    require('postcss-nested'),
    require('rebem-css'),
    require('postcss-url')({ url: 'rebase' }),
    require('autoprefixer')(),
    require('postcss-reporter')(),
  ]/*}}}*/
;

module.exports = function override(config/* , env */) {
  // use any rewires here ;-) You are welcome!

  // config = rewireTypescript(config, env);

  config = rewirePostcss(config, {
    parser: require('postcss-scss'),
    plugins: () => postcssPlugins,
  });

  return config;
};

const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: (config) => {
    config.module
      .rule("typescript")
      .test(/\.ts$/)
      .use("ts-loader")
      .loader("ts-loader")
      .options({
        transpileOnly: true,
        appendTsSuffixTo: [/\.vue$/],
      })
      .end();
  },
});

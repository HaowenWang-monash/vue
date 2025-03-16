import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  base: "/",  // 确保路径正确
  plugins: [vue()],
  build: {
    outDir: "dist",  // 指定构建目录
  },
});

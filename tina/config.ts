import { defineConfig } from "tinacms";

export default defineConfig({
  branch: "main",
  clientId: null,
  token: null,
  build: {
    outputFolder: "admin",
    publicFolder: "public",
  },
  media: {
    tina: {
      mediaRoot: "images",
      publicFolder: "public",
    },
  },
  schema: {
    collections: [
      {
        name: "post",
        label: "Blog Posts",
        path: "src/content/blog",
        format: "md",
        fields: [
          { type: "string", name: "title", label: "Title", isTitle: true, required: true },
          { type: "string", name: "description", label: "Meta Description", required: true },
          { type: "datetime", name: "pubDate", label: "Publish Date", required: true },
          { type: "string", name: "author", label: "Author" },
          { type: "string", name: "category", label: "Category" },
          { type: "image", name: "image", label: "Featured Image (Google Discover)" },
          { type: "string", name: "imageAlt", label: "Image Alt Text" },
          { type: "rich-text", name: "body", label: "Body", isBody: true },
        ],
      },
    ],
  },
});

module Jekyll
  module ApiDocGenerate
    def my_own_generate(apis)
      apis_docs = apis.group_by(&:category).map do |grouped_key, grouped_values|
        api_category = "## #{grouped_key}"

        api_items = grouped_values.map do |value|
          api_link = "### [#{value.name}](#{value.url})"
          code_snippets = value.code_snippets.map do |code_snippet_name, code_snippet_path|
            code_snippet_title = "#### Code Example: #{code_snippet_name}"
            code_snippet = File.read("_code_snippets/#{code_snippet_path}")
            code_snippet = "```python\n#{code_snippet}\n```"
            [code_snippet_title, code_snippet]
          end

          [api_link, code_snippets]
        end

        [api_category, api_items]
      end

      apis_docs.flatten.join("\n")
    end
  end
end

Liquid::Template.register_filter(Jekyll::ApiDocGenerate)

function CodeBlock(el)
  if el.attr and el.attr.identifier and el.attr.identifier ~= "" then
    print("Applying code-summary to:", el.attr.identifier) -- Debug message
    el.attr.attributes["code-summary"] = el.attr.identifier
  else
    print("No identifier found for a chunk.") -- Debug message
  end
  return el
end

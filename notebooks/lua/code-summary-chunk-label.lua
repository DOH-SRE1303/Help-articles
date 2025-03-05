function CodeBlock(el)
  local label = el.attributes["Label"] or el.attributes["label"]
  if label then
    el.attributes["code-summary"] = label
  end
  return el
end

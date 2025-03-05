function CodeBlock(el)
  -- Debugging: Print everything we can about the chunk
  print("=== DEBUG: FULL CHUNK DATA ===")
  print(el)

  -- Check if `el.meta` exists
  if el.meta then
    print("el.meta:", el.meta)
  end

  -- Check if `el.attr` contains attributes
  if el.attr then
    print("el.attr:", el.attr)
  end

  -- Check if `el.attr.attributes` contains any metadata
  if el.attr and el.attr.attributes then
    print("el.attr.attributes:", el.attr.attributes)
  end

  return el
end

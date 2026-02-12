const BOT_TOKEN = "Your-Bot-Token";
const CHANNELS = [
  { username: "@BotzEmpire", url: "https://t.me/BotzEmpire" },
  { username: "@Yaaro_kimehfill", url: "https://t.me/Yaaro_kimehfill" },
  { username: "@BotsDeal", url: "https://t.me/BotsDeal" }
];
const ADMINS = [7538572906]; // Yahan apna admin ID dalo

// Font conversion functions
const fontStyles = {
  typewriter: (text) => convertText(text, {
    'a': '𝚊', 'b': '𝚋', 'c': '𝚌', 'd': '𝚍', 'e': '𝚎', 'f': '𝚏', 'g': '𝚐', 'h': '𝚑', 'i': '𝚒', 'j': '𝚓',
    'k': '𝚔', 'l': '𝚕', 'm': '𝚖', 'n': '𝚗', 'o': '𝚘', 'p': '𝚙', 'q': '𝚚', 'r': '𝚛', 's': '𝚜', 't': '𝚝',
    'u': '𝚞', 'v': '𝚟', 'w': '𝚠', 'x': '𝚡', 'y': '𝚢', 'z': '𝚣',
    'A': '𝙰', 'B': '𝙱', 'C': '𝙲', 'D': '𝙳', 'E': '𝙴', 'F': '𝙵', 'G': '𝙶', 'H': '𝙷', 'I': '𝙸', 'J': '𝙹',
    'K': '𝙺', 'L': '𝙻', 'M': '𝙼', 'N': '𝙽', 'O': '𝙾', 'P': '𝙿', 'Q': '𝚀', 'R': '𝚁', 'S': '𝚂', 'T': '𝚃',
    'U': '𝚄', 'V': '𝚅', 'W': '𝚆', 'X': '𝚇', 'Y': '𝚈', 'Z': '𝚉'
  }),

  outline: (text) => convertText(text, {
    'a': '𝕒', 'b': '𝕓', 'c': '𝕔', 'd': '𝕕', 'e': '𝕖', 'f': '𝕗', 'g': '𝕘', 'h': '𝕙', 'i': '𝕚', 'j': '𝕛',
    'k': '𝕜', 'l': '𝕝', 'm': '𝕞', 'n': '𝕟', 'o': '𝕠', 'p': '𝕡', 'q': '𝕢', 'r': '𝕣', 's': '𝕤', 't': '𝕥',
    'u': '𝕦', 'v': '𝕧', 'w': '𝕨', 'x': '𝕩', 'y': '𝕪', 'z': '𝕫',
    'A': '𝔸', 'B': '𝔹', 'C': 'ℂ', 'D': '𝔻', 'E': '𝔼', 'F': '𝔽', 'G': '𝔾', 'H': 'ℍ', 'I': '𝕀', 'J': '𝕁',
    'K': '𝕂', 'L': '𝕃', 'M': '𝕄', 'N': 'ℕ', 'O': '𝕆', 'P': 'ℙ', 'Q': 'ℚ', 'R': 'ℝ', 'S': '𝕊', 'T': '𝕋',
    'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏', 'Y': '𝕐', 'Z': 'ℤ'
  }),

  serif: (text) => convertText(text, {
    'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡', 'i': '𝐢', 'j': '𝐣',
    'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧', 'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭',
    'u': '𝐮', 'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳',
    'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉',
    'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓',
    'U': '𝐔', 'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙'
  }),

  serif_bi: (text) => convertText(text, {
    'a': '𝒂', 'b': '𝒃', 'c': '𝒄', 'd': '𝒅', 'e': '𝒆', 'f': '𝒇', 'g': '𝒈', 'h': '𝒉', 'i': '𝒊', 'j': '𝒋',
    'k': '𝒌', 'l': '𝒍', 'm': '𝒎', 'n': '𝒏', 'o': '𝒐', 'p': '𝒑', 'q': '𝒒', 'r': '𝒓', 's': '𝒔', 't': '𝒕',
    'u': '𝒖', 'v': '𝒗', 'w': '𝒘', 'x': '𝒙', 'y': '𝒚', 'z': '𝒛',
    'A': '𝑨', 'B': '𝑩', 'C': '𝑪', 'D': '𝑫', 'E': '𝑬', 'F': '𝑭', 'G': '𝑮', 'H': '𝑯', 'I': '𝑰', 'J': '𝑱',
    'K': '𝑲', 'L': '𝑳', 'M': '𝑴', 'N': '𝑵', 'O': '𝑶', 'P': '𝑷', 'Q': '𝑸', 'R': '𝑹', 'S': '𝑺', 'T': '𝑻',
    'U': '𝑼', 'V': '𝑽', 'W': '𝑾', 'X': '𝑿', 'Y': '𝒀', 'Z': '𝒁'
  }),

  serif_i: (text) => convertText(text, {
    'a': '𝑎', 'b': '𝑏', 'c': '𝑐', 'd': '𝑑', 'e': '𝑒', 'f': '𝑓', 'g': '𝑔', 'h': 'ℎ', 'i': '𝑖', 'j': '𝑗',
    'k': '𝑘', 'l': '𝑙', 'm': '𝑚', 'n': '𝑛', 'o': '𝑜', 'p': '𝑝', 'q': '𝑞', 'r': '𝑟', 's': '𝑠', 't': '𝑡',
    'u': '𝑢', 'v': '𝑣', 'w': '𝑤', 'x': '𝑥', 'y': '𝑦', 'z': '𝑧',
    'A': '𝐴', 'B': '𝐵', 'C': '𝐶', 'D': '𝐷', 'E': '𝐸', 'F': '𝐹', 'G': '𝐺', 'H': '𝐻', 'I': '𝐼', 'J': '𝐽',
    'K': '𝐾', 'L': '𝐿', 'M': '𝑀', 'N': '𝑁', 'O': '𝑂', 'P': '𝑃', 'Q': '𝑄', 'R': '𝑅', 'S': '𝑆', 'T': '𝑇',
    'U': '𝑈', 'V': '𝑉', 'W': '𝑊', 'X': '𝑋', 'Y': '𝑌', 'Z': '𝑍'
  }),

  smallcaps: (text) => convertText(text, {
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ', 'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ',
    'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ',
    'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ',
    'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ', 'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ',
    'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ', 'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ',
    'U': 'ᴜ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ'
  }),

  script: (text) => convertText(text, {
    'a': '𝒶', 'b': '𝒷', 'c': '𝒸', 'd': '𝒹', 'e': '𝑒', 'f': '𝒻', 'g': '𝑔', 'h': '𝒽', 'i': '𝒾', 'j': '𝒿',
    'k': '𝓀', 'l': '𝓁', 'm': '𝓂', 'n': '𝓃', 'o': '𝑜', 'p': '𝓅', 'q': '𝓆', 'r': '𝓇', 's': '𝓈', 't': '𝓉',
    'u': '𝓊', 'v': '𝓋', 'w': '𝓌', 'x': '𝓍', 'y': '𝓎', 'z': '𝓏',
    'A': '𝒜', 'B': '𝐵', 'C': '𝒞', 'D': '𝒟', 'E': '𝐸', 'F': '𝐹', 'G': '𝒢', 'H': '𝐻', 'I': '𝐼', 'J': '𝒥',
    'K': '𝒦', 'L': '𝐿', 'M': '𝑀', 'N': '𝒩', 'O': '𝒪', 'P': '𝒫', 'Q': '𝒬', 'R': '𝑅', 'S': '𝒮', 'T': '𝒯',
    'U': '𝒰', 'V': '𝒱', 'W': '𝒲', 'X': '𝒳', 'Y': '𝒴', 'Z': '𝒵'
  }),

  script_b: (text) => convertText(text, {
    'a': '𝓪', 'b': '𝓫', 'c': '𝓬', 'd': '𝓭', 'e': '𝓮', 'f': '𝓯', 'g': '𝓰', 'h': '𝓱', 'i': '𝓲', 'j': '𝓳',
    'k': '𝓴', 'l': '𝓵', 'm': '𝓶', 'n': '𝓷', 'o': '𝓸', 'p': '𝓹', 'q': '𝓺', 'r': '𝓻', 's': '𝓼', 't': '𝓽',
    'u': '𝓾', 'v': '𝓿', 'w': '𝔀', 'x': '𝔁', 'y': '𝔂', 'z': '𝔃',
    'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓', 'E': '𝓔', 'F': '𝓕', 'G': '𝓖', 'H': '𝓗', 'I': '𝓘', 'J': '𝓙',
    'K': '𝓚', 'L': '𝓛', 'M': '𝓜', 'N': '𝓝', 'O': '𝓞', 'P': '𝓟', 'Q': '𝓠', 'R': '𝓡', 'S': '𝓢', 'T': '𝓣',
    'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧', 'Y': '𝓨', 'Z': '𝓩'
  }),

  tiny: (text) => convertText(text, {
    'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ᶦ', 'j': 'ʲ',
    'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ', 'p': 'ᵖ', 'q': 'ᑫ', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ',
    'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ',
    'A': 'ᴬ', 'B': 'ᴮ', 'C': 'ᶜ', 'D': 'ᴰ', 'E': 'ᴱ', 'F': 'ᶠ', 'G': 'ᴳ', 'H': 'ᴴ', 'I': 'ᴵ', 'J': 'ᴶ',
    'K': 'ᴷ', 'L': 'ᴸ', 'M': 'ᴹ', 'N': 'ᴺ', 'O': 'ᴼ', 'P': 'ᴾ', 'Q': 'Q', 'R': 'ᴿ', 'S': 'ˢ', 'T': 'ᵀ',
    'U': 'ᵁ', 'V': 'ⱽ', 'W': 'ᵂ', 'X': 'ˣ', 'Y': 'ʸ', 'Z': 'ᶻ'
  }),

  comic: (text) => convertText(text, {
    'a': 'ᗩ', 'b': 'ᗷ', 'c': 'ᑕ', 'd': 'ᗪ', 'e': 'E', 'f': 'ᖴ', 'g': 'G', 'h': 'ᕼ', 'i': 'I', 'j': 'ᒍ',
    'k': 'K', 'l': 'ᒪ', 'm': 'ᗰ', 'n': 'ᑎ', 'o': 'O', 'p': 'ᑭ', 'q': 'ᑫ', 'r': 'ᖇ', 's': 'ᔕ', 't': 'T',
    'u': 'ᑌ', 'v': 'ᐯ', 'w': 'ᗯ', 'x': '᙭', 'y': 'Y', 'z': 'ᘔ',
    'A': 'ᗩ', 'B': 'ᗷ', 'C': 'ᑕ', 'D': 'ᗪ', 'E': 'E', 'F': 'ᖴ', 'G': 'G', 'H': 'ᕼ', 'I': 'I', 'J': 'ᒍ',
    'K': 'K', 'L': 'ᒪ', 'M': 'ᗰ', 'N': 'ᑎ', 'O': 'O', 'P': 'ᑭ', 'Q': 'ᑫ', 'R': 'ᖇ', 'S': 'ᔕ', 'T': 'T',
    'U': 'ᑌ', 'V': 'ᐯ', 'W': 'ᗯ', 'X': '᙭', 'Y': 'Y', 'Z': 'ᘔ'
  }),

  sans_b: (text) => convertText(text, {
    'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵', 'i': '𝗶', 'j': '𝗷',
    'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿', 's': '𝘀', 't': '𝘁',
    'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅', 'y': '𝘆', 'z': '𝘇',
    'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜', 'J': '𝗝',
    'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥', 'S': '𝗦', 'T': '𝗧',
    'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭'
  }),

  sans_bi: (text) => convertText(text, {
    'a': '𝙖', 'b': '𝙗', 'c': '𝙘', 'd': '𝙙', 'e': '𝙚', 'f': '𝙛', 'g': '𝙜', 'h': '𝙝', 'i': '𝙞', 'j': '𝙟',
    'k': '𝙠', 'l': '𝙡', 'm': '𝙢', 'n': '𝙣', 'o': '𝙤', 'p': '𝙥', 'q': '𝙦', 'r': '𝙧', 's': '𝙨', 't': '𝙩',
    'u': '𝙪', 'v': '𝙫', 'w': '𝙬', 'x': '𝙭', 'y': '𝙮', 'z': '𝙯',
    'A': '𝘼', 'B': '𝘽', 'C': '𝘾', 'D': '𝘿', 'E': '𝙀', 'F': '𝙁', 'G': '𝙂', 'H': '𝙃', 'I': '𝙄', 'J': '𝙅',
    'K': '𝙆', 'L': '𝙇', 'M': '𝙈', 'N': '𝙉', 'O': '𝙊', 'P': '𝙋', 'Q': '𝙌', 'R': '𝙍', 'S': '𝙎', 'T': '𝙏',
    'U': '𝙐', 'V': '𝙑', 'W': '𝙒', 'X': '𝙓', 'Y': '𝙔', 'Z': '𝙕'
  }),

  sans_i: (text) => convertText(text, {
    'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧', 'g': '𝘨', 'h': '𝘩', 'i': '𝘪', 'j': '𝘫',
    'k': '𝘬', 'l': '𝘭', 'm': '𝘮', 'n': '𝘯', 'o': '𝘰', 'p': '𝘱', 'q': '𝘲', 'r': '𝘳', 's': '𝘴', 't': '𝘵',
    'u': '𝘶', 'v': '𝘷', 'w': '𝘸', 'x': '𝘹', 'y': '𝘺', 'z': '𝘻',
    'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍', 'G': '𝘎', 'H': '𝘏', 'I': '𝘐', 'J': '𝘑',
    'K': '𝘒', 'L': '𝘓', 'M': '𝘔', 'N': '𝘕', 'O': '𝘖', 'P': '𝘗', 'Q': '𝘘', 'R': '𝘙', 'S': '𝘚', 'T': '𝘛',
    'U': '𝘜', 'V': '𝘝', 'W': '𝘞', 'X': '𝘟', 'Y': '𝘠', 'Z': '𝘡'
  }),

  sans: (text) => convertText(text, {
    'a': '𝖺', 'b': '𝖻', 'c': '𝖼', 'd': '𝖽', 'e': '𝖾', 'f': '𝖿', 'g': '𝗀', 'h': '𝗁', 'i': '𝗂', 'j': '𝗃',
    'k': '𝗄', 'l': '𝗅', 'm': '𝗆', 'n': '𝗇', 'o': '𝗈', 'p': '𝗉', 'q': '𝗊', 'r': '𝗋', 's': '𝗌', 't': '𝗍',
    'u': '𝗎', 'v': '𝗏', 'w': '𝗐', 'x': '𝗑', 'y': '𝗒', 'z': '𝗓',
    'A': '𝖠', 'B': '𝖡', 'C': '𝖢', 'D': '𝖣', 'E': '𝖤', 'F': '𝖥', 'G': '𝖦', 'H': '𝖧', 'I': '𝖨', 'J': '𝖩',
    'K': '𝖪', 'L': '𝖫', 'M': '𝖬', 'N': '𝖭', 'O': '𝖮', 'P': '𝖯', 'Q': '𝖰', 'R': '𝖱', 'S': '𝖲', 'T': '𝖳',
    'U': '𝖴', 'V': '𝖵', 'W': '𝖶', 'X': '𝖷', 'Y': '𝖸', 'Z': '𝖹'
  }),

  circles: (text) => convertText(text, {
    'a': 'ⓐ', 'b': 'ⓑ', 'c': 'ⓒ', 'd': 'ⓓ', 'e': 'ⓔ', 'f': 'ⓕ', 'g': 'ⓖ', 'h': 'ⓗ', 'i': 'ⓘ', 'j': 'ⓙ',
    'k': 'ⓚ', 'l': 'ⓛ', 'm': 'ⓜ', 'n': 'ⓝ', 'o': 'ⓞ', 'p': 'ⓟ', 'q': 'ⓠ', 'r': 'ⓡ', 's': 'ⓢ', 't': 'ⓣ',
    'u': 'ⓤ', 'v': 'ⓥ', 'w': 'ⓦ', 'x': 'ⓧ', 'y': 'ⓨ', 'z': 'ⓩ',
    'A': 'Ⓐ', 'B': 'Ⓑ', 'C': 'Ⓒ', 'D': 'Ⓓ', 'E': 'Ⓔ', 'F': 'Ⓕ', 'G': 'Ⓖ', 'H': 'Ⓗ', 'I': 'Ⓘ', 'J': 'Ⓙ',
    'K': 'Ⓚ', 'L': 'Ⓛ', 'M': 'Ⓜ', 'N': 'Ⓝ', 'O': 'Ⓞ', 'P': 'Ⓟ', 'Q': 'Ⓠ', 'R': 'Ⓡ', 'S': 'Ⓢ', 'T': 'Ⓣ',
    'U': 'Ⓤ', 'V': 'Ⓥ', 'W': 'Ⓦ', 'X': 'Ⓧ', 'Y': 'Ⓨ', 'Z': 'Ⓩ'
  }),

  circles_2: (text) => convertText(text, {
    'a': '🅐', 'b': '🅑', 'c': '🅒', 'd': '🅓', 'e': '🅔', 'f': '🅕', 'g': '🅖', 'h': '🅗', 'i': '🅘', 'j': '🅙',
    'k': '🅚', 'l': '🅛', 'm': '🅜', 'n': '🅝', 'o': '🅞', 'p': '🅟', 'q': '🅠', 'r': '🅡', 's': '🅢', 't': '🅣',
    'u': '🅤', 'v': '🅥', 'w': '🅦', 'x': '🅧', 'y': '🅨', 'z': '🅩',
    'A': '🅐', 'B': '🅑', 'C': '🅒', 'D': '🅓', 'E': '🅔', 'F': '🅕', 'G': '🅖', 'H': '🅗', 'I': '🅘', 'J': '🅙',
    'K': '🅚', 'L': '🅛', 'M': '🅜', 'N': '🅝', 'O': '🅞', 'P': '🅟', 'Q': '🅠', 'R': '🅡', 'S': '🅢', 'T': '🅣',
    'U': '🅤', 'V': '🅥', 'W': '🅦', 'X': '🅧', 'Y': '🅨', 'Z': '🅩'
  }),

  gothic: (text) => convertText(text, {
    'a': '𝔞', 'b': '𝔟', 'c': '𝔠', 'd': '𝔡', 'e': '𝔢', 'f': '𝔣', 'g': '𝔤', 'h': '𝔥', 'i': '𝔦', 'j': '𝔧',
    'k': '𝔨', 'l': '𝔩', 'm': '𝔪', 'n': '𝔫', 'o': '𝔬', 'p': '𝔭', 'q': '𝔮', 'r': '𝔯', 's': '𝔰', 't': '𝔱',
    'u': '𝔲', 'v': '𝔳', 'w': '𝔴', 'x': '𝔵', 'y': '𝔶', 'z': '𝔷',
    'A': '𝔄', 'B': '𝔅', 'C': 'ℭ', 'D': '𝔇', 'E': '𝔈', 'F': '𝔉', 'G': '𝔊', 'H': 'ℌ', 'I': 'ℑ', 'J': '𝔍',
    'K': '𝔎', 'L': '𝔏', 'M': '𝔐', 'N': '𝔑', 'O': '𝔒', 'P': '𝔓', 'Q': '𝔔', 'R': 'ℜ', 'S': '𝔖', 'T': '𝔗',
    'U': '𝔘', 'V': '𝔙', 'W': '𝔚', 'X': '𝔛', 'Y': '𝔜', 'Z': 'ℨ'
  }),

  gothic_b: (text) => convertText(text, {
    'a': '𝖆', 'b': '𝖇', 'c': '𝖈', 'd': '𝖉', 'e': '𝖊', 'f': '𝖋', 'g': '𝖌', 'h': '𝖍', 'i': '𝖎', 'j': '𝖏',
    'k': '𝖐', 'l': '𝖑', 'm': '𝖒', 'n': '𝖓', 'o': '𝖔', 'p': '𝖕', 'q': '𝖖', 'r': '𝖗', 's': '𝖘', 't': '𝖙',
    'u': '𝖚', 'v': '𝖛', 'w': '𝖜', 'x': '𝖝', 'y': '𝖞', 'z': '𝖟',
    'A': '𝕬', 'B': '𝕭', 'C': '𝕮', 'D': '𝕯', 'E': '𝕰', 'F': '𝕱', 'G': '𝕲', 'H': '𝕳', 'I': '𝕴', 'J': '𝕵',
    'K': '𝕶', 'L': '𝕷', 'M': '𝕸', 'N': '𝕹', 'O': '𝕺', 'P': '𝕻', 'Q': '𝕼', 'R': '𝕽', 'S': '𝕾', 'T': '𝕿',
    'U': '𝖀', 'V': '𝖁', 'W': '𝖂', 'X': '𝖃', 'Y': '𝖄', 'Z': '𝖅'
  }),

  special: (text) => convertText(text, {
    'a': '🇦', 'b': '🇧', 'c': '🇨', 'd': '🇩', 'e': '🇪', 'f': '🇫', 'g': '🇬', 'h': '🇭', 'i': '🇮', 'j': '🇯',
    'k': '🇰', 'l': '🇱', 'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵', 'q': '🇶', 'r': '🇷', 's': '🇸', 't': '🇹',
    'u': '🇺', 'v': '🇻', 'w': '🇼', 'x': '🇽', 'y': '🇾', 'z': '🇿',
    'A': '🇦', 'B': '🇧', 'C': '🇨', 'D': '🇩', 'E': '🇪', 'F': '🇫', 'G': '🇬', 'H': '🇭', 'I': '🇮', 'J': '🇯',
    'U': '🇺', 'V': '🇻', 'W': '🇼', 'X': '🇽', 'Y': '🇾', 'Z': '🇿'
  }), 'K': '🇰', 'L': '🇱', 'M': '🇲', 'N': '🇳', 'O': '🇴', 'P': '🇵', 'Q': '🇶', 'R': '🇷', 'S': '🇸', 'T': '🇹',
   

  squares: (text) => convertText(text, {
    'a': '🄰', 'b': '🄱', 'c': '🄲', 'd': '🄳', 'e': '🄴', 'f': '🄵', 'g': '🄶', 'h': '🄷', 'i': '🄸', 'j': '🄹',
    'k': '🄺', 'l': '🄻', 'm': '🄼', 'n': '🄽', 'o': '🄾', 'p': '🄿', 'q': '🅀', 'r': '🅁', 's': '🅂', 't': '🅃',
    'u': '🅄', 'v': '🅅', 'w': '🅆', 'x': '🅇', 'y': '🅈', 'z': '🅉',
    'A': '🄰', 'B': '🄱', 'C': '🄲', 'D': '🄳', 'E': '🄴', 'F': '🄵', 'G': '🄶', 'H': '🄷', 'I': '🄸', 'J': '🄹',
    'K': '🄺', 'L': '🄻', 'M': '🄼', 'N': '🄽', 'O': '🄾', 'P': '🄿', 'Q': '🅀', 'R': '🅁', 'S': '🅂', 'T': '🅃',
    'U': '🅄', 'V': '🅅', 'W': '🅆', 'X': '🅇', 'Y': '🅈', 'Z': '🅉'
  }),

  squares_2: (text) => convertText(text, {
    'a': '🅰', 'b': '🅱', 'c': '🅲', 'd': '🅳', 'e': '🅴', 'f': '🅵', 'g': '🅶', 'h': '🅷', 'i': '🅸', 'j': '🅹',
    'k': '🅺', 'l': '🅻', 'm': '🅼', 'n': '🅽', 'o': '🅾', 'p': '🅿', 'q': '🆀', 'r': '🆁', 's': '🆂', 't': '🆃',
    'u': '🆄', 'v': '🆅', 'w': '🆆', 'x': '🆇', 'y': '🆈', 'z': '🆉',
    'A': '🅰', 'B': '🅱', 'C': '🅲', 'D': '🅳', 'E': '🅴', 'F': '🅵', 'G': '🅶', 'H': '🅷', 'I': '🅸', 'J': '🅹',
    'K': '🅺', 'L': '🅻', 'M': '🅼', 'N': '🅽', 'O': '🅾', 'P': '🅿', 'Q': '🆀', 'R': '🆁', 'S': '🆂', 'T': '🆃',
    'U': '🆄', 'V': '🆅', 'W': '🆆', 'X': '🆇', 'Y': '🆈', 'Z': '🆉'
  }),

  andalucia: (text) => convertText(text, {
    'a': 'ꪖ', 'b': '᥇', 'c': 'ᥴ', 'd': 'ᦔ', 'e': 'ꫀ', 'f': 'ᠻ', 'g': 'ᧁ', 'h': 'ꫝ', 'i': '𝓲', 'j': '᧒',
    'k': '𝘬', 'l': 'ꪶ', 'm': 'ꪑ', 'n': 'ꪀ', 'o': 'ꪮ', 'p': 'ᩏ', 'q': 'ᠳ', 'r': '𝘳', 's': 'ꪜ', 't': 'ᥴ',
    'u': 'ꪊ', 'v': 'ꪜ', 'w': '᭙', 'x': '᥊', 'y': 'ꪗ', 'z': 'ɀ',
    'A': 'ꪖ', 'B': '᥇', 'C': 'ᥴ', 'D': 'ᦔ', 'E': 'ꫀ', 'F': 'ᠻ', 'G': 'ᧁ', 'H': 'ꫝ', 'I': '𝓲', 'J': '᧒',
    'K': '𝘬', 'L': 'ꪶ', 'M': 'ꪑ', 'N': 'ꪀ', 'O': 'ꪮ', 'P': 'ᩏ', 'Q': 'ᠳ', 'R': '𝘳', 'S': 'ꪜ', 'T': 'ᥴ',
    'U': 'ꪊ', 'V': 'ꪜ', 'W': '᭙', 'X': '᥊', 'Y': 'ꪗ', 'Z': 'ɀ'
  }),

  manga: (text) => convertText(text, {
    'a': '卂', 'b': '乃', 'c': '匚', 'd': 'ᗪ', 'e': '乇', 'f': '千', 'g': 'Ꮆ', 'h': '卄', 'i': '丨', 'j': 'ﾌ',
    'k': 'Ҝ', 'l': 'ㄥ', 'm': '爪', 'n': '几', 'o': 'ㄖ', 'p': '卩', 'q': 'Ɋ', 'r': '尺', 's': '丂', 't': 'ㄒ',
    'u': 'ㄩ', 'v': 'ᐯ', 'w': '山', 'x': '乂', 'y': 'ㄚ', 'z': '乙',
    'A': '卂', 'B': '乃', 'C': '匚', 'D': 'ᗪ', 'E': '乇', 'F': '千', 'G': 'Ꮆ', 'H': '卄', 'I': '丨', 'J': 'ﾌ',
    'K': 'Ҝ', 'L': 'ㄥ', 'M': '爪', 'N': '几', 'O': 'ㄖ', 'P': '卩', 'Q': 'Ɋ', 'R': '尺', 'S': '丂', 'T': 'ㄒ',
    'U': 'ㄩ', 'V': 'ᐯ', 'W': '山', 'X': '乂', 'Y': 'ㄚ', 'Z': '乙'
  }),

  ladybug: (text) => convertText(text, {
    'a': 'ꍏ', 'b': 'ꌃ', 'c': 'ꏳ', 'd': 'ꀷ', 'e': 'ꍟ', 'f': 'ꎇ', 'g': 'ꁅ', 'h': 'ꁝ', 'i': 'ꀤ', 'j': 'ꀭ',
    'k': 'ꀘ', 'l': '꒒', 'm': 'ꎭ', 'n': 'ꈤ', 'o': 'ꂦ', 'p': 'ᖘ', 'q': 'ꆰ', 'r': 'ꋪ', 's': 'ꌚ', 't': '꓄',
    'u': 'ꀎ', 'v': 'ꏝ', 'w': 'ꅐ', 'x': 'ꉧ', 'y': 'ꌩ', 'z': 'ꁴ',
    'A': 'ꍏ', 'B': 'ꌃ', 'C': 'ꏳ', 'D': 'ꀷ', 'E': 'ꍟ', 'F': 'ꎇ', 'G': 'ꁅ', 'H': 'ꁝ', 'I': 'ꀤ', 'J': 'ꀭ',
    'K': 'ꀘ', 'L': '꒒', 'M': 'ꎭ', 'N': 'ꈤ', 'O': 'ꂦ', 'P': 'ᖘ', 'Q': 'ꆰ', 'R': 'ꋪ', 'S': 'ꌚ', 'T': '꓄',
    'U': 'ꀎ', 'V': 'ꏝ', 'W': 'ꅐ', 'X': 'ꉧ', 'Y': 'ꌩ', 'Z': 'ꁴ'
  }),

  stop: (text) => convertText(text, {
    'a': 'a⃠', 'b': 'b⃠', 'c': 'c⃠', 'd': 'd⃠', 'e': 'e⃠', 'f': 'f⃠', 'g': 'g⃠', 'h': 'h⃠', 'i': 'i⃠', 'j': 'j⃠',
    'k': 'k⃠', 'l': 'l⃠', 'm': 'm⃠', 'n': 'n⃠', 'o': 'o⃠', 'p': 'p⃠', 'q': 'q⃠', 'r': 'r⃠', 's': 's⃠', 't': 't⃠',
    'u': 'u⃠', 'v': 'v⃠', 'w': 'w⃠', 'x': 'x⃠', 'y': 'y⃠', 'z': 'z⃠',
    'A': 'A⃠', 'B': 'B⃠', 'C': 'C⃠', 'D': 'D⃠', 'E': 'E⃠', 'F': 'F⃠', 'G': 'G⃠', 'H': 'H⃠', 'I': 'I⃠', 'J': 'J⃠',
    'K': 'K⃠', 'L': 'L⃠', 'M': 'M⃠', 'N': 'N⃠', 'O': 'O⃠', 'P': 'P⃠', 'Q': 'Q⃠', 'R': 'R⃠', 'S': 'S⃠', 'T': 'T⃠',
    'U': 'U⃠', 'V': 'V⃠', 'W': 'W⃠', 'X': 'X⃠', 'Y': 'Y⃠', 'Z': 'Z⃠'
  }),

  rvnes: (text) => convertText(text, {
    'a': 'ጀ', 'b': 'ፕ', 'c': 'ር', 'd': 'ዘ', 'e': 'ቿ', 'f': 'ዞ', 'g': 'ኗ', 'h': 'ዕ', 'i': 'ጎ', 'j': 'ጋ',
    'k': 'ጕ', 'l': 'ረ', 'm': 'ጠ', 'n': 'ክ', 'o': 'ዐ', 'p': 'መ', 'q': 'ዒ', 'r': 'ዪ', 's': 'ነ', 't': 'ፕ',
    'u': 'ሁ', 'v': 'ሀ', 'w': 'Ꭷ', 'x': 'ሸ', 'y': 'ሃ', 'z': 'ጊ',
    'A': 'ጀ', 'B': 'ፕ', 'C': 'ር', 'D': 'ዘ', 'E': 'ቿ', 'F': 'ዞ', 'G': 'ኗ', 'H': 'ዕ', 'I': 'ጎ', 'J': 'ጋ',
    'K': 'ጕ', 'L': 'ረ', 'M': 'ጠ', 'N': 'ክ', 'O': 'ዐ', 'P': 'መ', 'Q': 'ዒ', 'R': 'ዪ', 'S': 'ነ', 'T': 'ፕ',
    'U': 'ሁ', 'V': 'ሀ', 'W': 'Ꭷ', 'X': 'ሸ', 'Y': 'ሃ', 'Z': 'ጊ'
  }),

  frozen: (text) => convertText(text, {
    'a': 'a༙', 'b': 'b༙', 'c': 'c༙', 'd': 'd༙', 'e': 'e༙', 'f': 'f༙', 'g': 'g༙', 'h': 'h༙', 'i': 'i༙', 'j': 'j༙',
    'k': 'k༙', 'l': 'l༙', 'm': 'm༙', 'n': 'n༙', 'o': 'o༙', 'p': 'p༙', 'q': 'q༙', 'r': 'r༙', 's': 's༙', 't': 't༙',
    'u': 'u༙', 'v': 'v༙', 'w': 'w༙', 'x': 'x༙', 'y': 'y༙', 'z': 'z༙',
    'A': 'A༙', 'B': 'B༙', 'C': 'C༙', 'D': 'D༙', 'E': 'E༙', 'F': 'F༙', 'G': 'G༙', 'H': 'H༙', 'I': 'I༙', 'J': 'J༙',
    'K': 'K༙', 'L': 'L༙', 'M': 'M༙', 'N': 'N༙', 'O': 'O༙', 'P': 'P༙', 'Q': 'Q༙', 'R': 'R༙', 'S': 'S༙', 'T': 'T༙',
    'U': 'U༙', 'V': 'V༙', 'W': 'W༙', 'X': 'X༙', 'Y': 'Y༙', 'Z': 'Z༙'
  }),

  clouds: (text) => convertText(text, {
    'a': 'a͜͡', 'b': 'b͜͡', 'c': 'c͜͡', 'd': 'd͜͡', 'e': 'e͜͡', 'f': 'f͜͡', 'g': 'g͜͡', 'h': 'h͜͡', 'i': 'i͜͡', 'j': 'j͜͡',
    'k': 'k͜͡', 'l': 'l͜͡', 'm': 'm͜͡', 'n': 'n͜͡', 'o': 'o͜͡', 'p': 'p͜͡', 'q': 'q͜͡', 'r': 'r͜͡', 's': 's͜͡', 't': 't͜͡',
    'u': 'u͜͡', 'v': 'v͜͡', 'w': 'w͜͡', 'x': 'x͜͡', 'y': 'y͜͡', 'z': 'z͜͡',
    'A': 'A͜͡', 'B': 'B͜͡', 'C': 'C͜͡', 'D': 'D͜͡', 'E': 'E͜͡', 'F': 'F͜͡', 'G': 'G͜͡', 'H': 'H͜͡', 'I': 'I͜͡', 'J': 'J͜͡',
    'K': 'K͜͡', 'L': 'L͜͡', 'M': 'M͜͡', 'N': 'N͜͡', 'O': 'O͜͡', 'P': 'P͜͡', 'Q': 'Q͜͡', 'R': 'R͜͡', 'S': 'S͜͡', 'T': 'T͜͡',
    'U': 'U͜͡', 'V': 'V͜͡', 'W': 'W͜͡', 'X': 'X͜͡', 'Y': 'Y͜͡', 'Z': 'Z͜͡'
  }),

  happy: (text) => convertText(text, {
    'a': 'ă̈', 'b': 'b̆̈', 'c': 'c̆̈', 'd': 'd̆̈', 'e': 'ĕ̈', 'f': 'f̆̈', 'g': 'ğ̈', 'h': 'h̆̈', 'i': 'ĭ̈', 'j': 'j̆̈',
    'k': 'k̆̈', 'l': 'l̆̈', 'm': 'm̆̈', 'n': 'n̆̈', 'o': 'ŏ̈', 'p': 'p̆̈', 'q': 'q̆̈', 'r': 'r̆̈', 's': 's̆̈', 't': 't̆̈',
    'u': 'ŭ̈', 'v': 'v̆̈', 'w': 'w̆̈', 'x': 'x̆̈', 'y': 'y̆̈', 'z': 'z̆̈',
    'A': 'Ă̈', 'B': 'B̆̈', 'C': 'C̆̈', 'D': 'D̆̈', 'E': 'Ĕ̈', 'F': 'F̆̈', 'G': 'Ğ̈', 'H': 'H̆̈', 'I': 'Ĭ̈', 'J': 'J̆̈',
    'K': 'K̆̈', 'L': 'L̆̈', 'M': 'M̆̈', 'N': 'N̆̈', 'O': 'Ŏ̈', 'P': 'P̆̈', 'Q': 'Q̆̈', 'R': 'R̆̈', 'S': 'S̆̈', 'T': 'T̆̈',
    'U': 'Ŭ̈', 'V': 'V̆̈', 'W': 'W̆̈', 'X': 'X̆̈', 'Y': 'Y̆̈', 'Z': 'Z̆̈'
  }),

  sad: (text) => convertText(text, {
    'a': 'ȃ̈', 'b': 'b̑̈', 'c': 'c̑̈', 'd': 'd̑̈', 'e': 'ȇ̈', 'f': 'f̑̈', 'g': 'g̑̈', 'h': 'h̑̈', 'i': 'ȋ̈', 'j': 'j̑̈',
    'k': 'k̑̈', 'l': 'l̑̈', 'm': 'm̑̈', 'n': 'n̑̈', 'o': 'ȏ̈', 'p': 'p̑̈', 'q': 'q̑̈', 'r': 'ȓ̈', 's': 's̑̈', 't': 't̑̈',
    'u': 'ȗ̈', 'v': 'v̑̈', 'w': 'w̑̈', 'x': 'x̑̈', 'y': 'y̑̈', 'z': 'z̑̈',
    'A': 'Ȃ̈', 'B': 'B̑̈', 'C': 'C̑̈', 'D': 'D̑̈', 'E': 'Ȇ̈', 'F': 'F̑̈', 'G': 'G̑̈', 'H': 'H̑̈', 'I': 'Ȋ̈', 'J': 'J̑̈',
    'K': 'K̑̈', 'L': 'L̑̈', 'M': 'M̑̈', 'N': 'N̑̈', 'O': 'Ȏ̈', 'P': 'P̑̈', 'Q': 'Q̑̈', 'R': 'Ȓ̈', 'S': 'S̑̈', 'T': 'T̑̈',
    'U': 'Ȗ̈', 'V': 'V̑̈', 'W': 'W̑̈', 'X': 'X̑̈', 'Y': 'Y̑̈', 'Z': 'Z̑̈'
  }),

  // New font added as requested
  newfont: (text) => convertText(text, {
    'a': 'ᴧ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'є', 'f': 'ғ', 'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ',
    'k': 'ᴋ', 'l': 'ʟ', 'm': 'ϻ', 'n': 'η', 'o': 'σ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ꝛ', 's': 's', 't': 'ᴛ',
    'u': 'υ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ',
    'A': 'ᴧ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'є', 'F': 'ғ', 'G': 'ɢ', 'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ',
    'K': 'ᴋ', 'L': 'ʟ', 'M': 'ϻ', 'N': 'η', 'O': 'σ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ꝛ', 'S': 's', 'T': 'ᴛ',
    'U': 'υ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ'
  })
};

// Helper function for text conversion
function convertText(text, map) {
  return text.split('').map(char => map[char] || char).join('');
}

// Store user text temporarily (in-memory, will reset on worker restart)
const userTexts = new Map();

// Font buttons layout
const fontButtons = [
  [
    { text: "ɴᴇᴡꜰᴏɴᴛ", callback_data: "newfont" },
  ],
  [
    { text: "𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛", callback_data: "typewriter" },
    { text: "𝕆𝕦𝕝𝕚𝕟𝕖", callback_data: "outline" },
    { text: "𝐒𝐞𝐫𝐢𝐟", callback_data: "serif" }
  ],
  [
    { text: "𝑺𝒆𝒓𝒊𝒇", callback_data: "serif_bi" },
    { text: "𝑆𝑒𝑟𝑖𝑓", callback_data: "serif_i" },
    { text: "Sᴍᴀʟʟ Cᴀᴘs", callback_data: "smallcaps" }
  ],
  [
    { text: "𝓈𝒸𝓇𝒾𝓅𝓉", callback_data: "script" },
    { text: "𝓼𝓬𝓻𝓲𝓹𝓽", callback_data: "script_b" },
    { text: "ᵗⁱⁿʸ", callback_data: "tiny" }
  ],
  [
    { text: "ᑕOᗰIᑕ", callback_data: "comic" },
    { text: "𝗦𝗮𝗻𝘀", callback_data: "sans_b" },
    { text: "𝙎𝙖𝙣𝙨", callback_data: "sans_bi" }
  ],
  [
    { text: "𝘚𝘢𝘯𝘴", callback_data: "sans_i" },
    { text: "𝖲𝖺𝗇𝗌", callback_data: "sans" },
    { text: "Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎", callback_data: "circles" }
  ],
  [
    { text: "🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎", callback_data: "circles_2" },
    { text: "𝔊𝔬𝔱𝔥𝔦𝔠", callback_data: "gothic" },
    { text: "𝕲𝖔𝖙𝖍𝖎𝖈", callback_data: "gothic_b" }
  ],
  [
    { text: "🇸 🇵 🇪 🇨 🇮 🇦 🇱 ", callback_data: "special" },
    { text: "🅂🅀🅄🄰🅁🄴🅂", callback_data: "squares" },
    { text: "🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎", callback_data: "squares_2" }
  ],
  [
    { text: "ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ", callback_data: "andalucia" },
    { text: "爪卂几ᘜ卂", callback_data: "manga" },
    { text: "꒒ꍏꀷꌩꌃꀎꁅ", callback_data: "ladybug" }
  ],
  [
    { text: "S⃠t⃠o⃠p⃠", callback_data: "stop" },
    { text: "ዪሀክቿነ", callback_data: "rvnes" },
    { text: "F༙r༙o༙z༙e༙n༙", callback_data: "frozen" }
  ],
  [
    { text: "C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡", callback_data: "clouds" },
    { text: "H̆̈ă̈p̆̈p̆̈y", callback_data: "happy" },
    { text: "S̑̈ȃ̈d̑̈", callback_data: "sad" }
  ],
  [
    { text: "🔄 New Text", callback_data: "new_text" },
    { text: "❌ Clear", callback_data: "clear" }
  ]
];

const fButtons = [
  [
    { text: "ηєᴡ ᴛєxᴛ ⌯", callback_data: "new_text" },
  ],
  [
    { text: "˹ υᴘᴅᴧᴛєs ˼", url: "https://t.me/anshapi" },
    { text: "˹ sυᴘᴘσʀᴛ ˼", url: "https://t.me/revangeapi" }
  ],
  [
    { text: "˹ ᴧʟʟ ʙσᴛs ˼ ", url: "https://t.me/nenobots" },
    { text: "˹ υᴘᴅᴧᴛєs ˼", url: "https://t.me/vip_robotz" },
  ],
];


// Force join buttons
const forceJoinButtons = [
  [
    { text: "📢 Join ", url: "https://t.me/anshapi" },
    { text: "📢 Join ", url: "https://t.me/revangeapi" }
  ],
  [
    { text: "📢 Join ", url: "https://t.me/nenobots" },
  ],
  [
    { text: "✅ Check Membership", callback_data: "check_join" }
  ]
];

// Check if user is joined to required channels
async function checkChannels(userId) {
  try {
    for (const channel of CHANNELS) {
      const response = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/getChatMember?chat_id=${channel.username}&user_id=${userId}`);
      const data = await response.json();
      if (!data.ok || (data.result.status !== 'member' && data.result.status !== 'administrator' && data.result.status !== 'creator')) {
        return false;
      }
    }
    return true;
  } catch (error) {
    console.error('Error checking channels:', error);
    return true; // If there's an error, allow user to proceed
  }
}

// Send channel join message with inline buttons
function getChannelJoinMessage() {
  let message = "🔒 *Channel Membership Required* 🔒\n\n";
  message += "📢 *To use this bot, please join our channels first:*\n\n";
  
  CHANNELS.forEach((channel, index) => {
    message += `📌 *Channel ${index + 1}:* ${channel.username}\n`;
  });
  
  message += "\n👉 After joining all channels, click *'Check Membership'* below!";
  
  return message;
}

// Telegram API functions
async function sendMessage(chatId, text, parse_mode, reply_markup = null) {
  const url = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;
  const body = {
    chat_id: chatId,
    text: text,
    parse_mode: parse_mode
  };
  
  if (reply_markup) {
    body.reply_markup = reply_markup;
  }
  
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
  
  return await response.json();
}

async function editMessage(chatId, messageId, text, parse_mode, reply_markup = null) {
  const url = `https://api.telegram.org/bot${BOT_TOKEN}/editMessageText`;
  const body = {
    chat_id: chatId,
    message_id: messageId,
    text: text,
    parse_mode: parse_mode
  };
  
  if (reply_markup) {
    body.reply_markup = reply_markup;
  }
  
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
  
  return await response.json();
}

async function answerCallbackQuery(callbackQueryId, text = "") {
  const url = `https://api.telegram.org/bot${BOT_TOKEN}/answerCallbackQuery`;
  const body = {
    callback_query_id: callbackQueryId
  };
  
  if (text) {
    body.text = text;
    body.show_alert = true;
  }
  
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
  
  return await response.json();
}

// Extract text from message for callback queries
function extractTextFromMessage(message) {
  if (!message || !message.text) return null;
  
  // Remove the bot's response prefix to get original user text
  const lines = message.text.split('\n');
  for (const line of lines) {
    if (line.includes('Original Text:') || line.includes('Your Text:')) {
      const textMatch = line.match(/`([^`]+)`/);
      if (textMatch && textMatch[1]) {
        return textMatch[1];
      }
    }
  }
  
  // If no formatted text found, return the raw message text
  return message.text.replace(/📝 \*Your Text:\*\s*`?|`/g, '').trim();
}

// Main bot function
async function handleUpdate(update) {
  if (!update.message && !update.callback_query) {
    return new Response('OK');
  }
  
  const userId = update.message ? update.message.from.id : update.callback_query.from.id;
  const chatId = update.message ? update.message.chat.id : update.callback_query.message.chat.id;
  
  // Check channels membership
  const isJoined = await checkChannels(userId);
  
  if (update.message) {
    const message = update.message;
    
    // Handle commands
    if (message.text && message.text.startsWith('/')) {
      const command = message.text.split(' ')[0];
      
      if (command === '/start') {
        if (!isJoined) {
          await sendMessage(chatId, getChannelJoinMessage(), "Markdown", {
            inline_keyboard: forceJoinButtons
          });
          return new Response('OK');
        }
        
        const welcomeText = `🎨 *Welcome to Advanced Font Changer Bot!*

✨ *30+ Font Styles Available*
• Fancy Fonts • Stylish Text • Cool Letters

📝 *How to Use:*
1. Send me any text
2. Choose your favorite font style
3. Copy and use anywhere!

Send me any text to get started!`;

        await sendMessage(chatId, welcomeText, "Markdown", {
          inline_keyboard: fButtons
        });
        return new Response('OK');
      }
      
      if (command === '/broadcast') {
        if (!ADMINS.includes(userId)) {
          await sendMessage(chatId, "❌ *You are not authorized to use this command!*", "Markdown");
          return new Response('OK');
        }
        
        const broadcastText = message.text.replace('/broadcast', '').trim();
        if (!broadcastText) {
          await sendMessage(chatId, "❌ *Please provide a message to broadcast!*\nUsage: `/broadcast your message`", "Markdown");
          return new Response('OK');
        }
        
        // Simple broadcast implementation
        await sendMessage(chatId, `📢 *Broadcast Sent:*\n\n${broadcastText}`, "Markdown");
        return new Response('OK');
      }
    }
    
    // Handle text messages
    if (message.text && !message.text.startsWith('/')) {
      if (!isJoined) {
        await sendMessage(chatId, getChannelJoinMessage(), "Markdown", {
          inline_keyboard: forceJoinButtons
        });
        return new Response('OK');
      }
      
      // Store user's text
      userTexts.set(userId, message.text);
      
      const responseText = `📝 *Your Text:* \`${message.text}\`

🎨 *Select a font style to convert your text:*`;

      await sendMessage(chatId, responseText, "Markdown", {
        inline_keyboard: fontButtons
      });
      return new Response('OK');
    }
  }
  
  if (update.callback_query) {
    const callback = update.callback_query;
    const data = callback.data;
    const messageId = callback.message.message_id;
    const messageText = callback.message.text;
    
    // Handle check_join callback
    if (data === "check_join") {
      const isJoinedNow = await checkChannels(userId);
      
      if (isJoinedNow) {
        await answerCallbackQuery(callback.id, "✅ Great! You have joined all channels. Now you can use the bot!");
        
        const welcomeText = `🎉 *Welcome! Membership Verified* ✅

🎨 *Now you can use the Font Changer Bot!*

✨ *30+ Font Styles Available*
• Send any text and choose your favorite font style!

Send me any text to get started!`;
        
        await editMessage(chatId, messageId, welcomeText, "Markdown", {
          inline_keyboard: fontButtons
        });
      } else {
        await answerCallbackQuery(callback.id, "❌ You haven't joined all channels yet. Please join all channels and try again.");
        
        await editMessage(chatId, messageId, getChannelJoinMessage(), "Markdown", {
          inline_keyboard: forceJoinButtons
        });
      }
      return new Response('OK');
    }
    
    // For other callbacks, check membership first
    if (!isJoined) {
      await answerCallbackQuery(callback.id, "❌ Please join all channels first to use this feature!");
      
      await editMessage(chatId, messageId, getChannelJoinMessage(), "Markdown", {
        inline_keyboard: forceJoinButtons
      });
      return new Response('OK');
    }
    
    // Get user text from storage OR extract from current message
    let userText = userTexts.get(userId);
    
    // If text not found in storage, try to extract from current message
    if (!userText && messageText) {
      userText = extractTextFromMessage(callback.message);
      if (userText) {
        userTexts.set(userId, userText); // Store it for future use
      }
    }
    
    // Answer callback query
    await answerCallbackQuery(callback.id);
    
    if (data === "new_text") {
      await editMessage(chatId, messageId, "📝 *Please send me your new text:*", "Markdown");
      return new Response('OK');
    }
    
    if (data === "clear") {
      userTexts.delete(userId);
      await editMessage(chatId, messageId, "🗑️ *Text cleared! Send me new text to continue.*", "Markdown", {
        inline_keyboard: fontButtons
      });
      return new Response('OK');
    }
    
    if (!userText) {
      await editMessage(chatId, messageId, "❌ *No text found! Please send me text first.*", "Markdown", {
        inline_keyboard: fontButtons
      });
      return new Response('OK');
    }
    
    if (fontStyles[data]) {
      const convertedText = fontStyles[data](userText);
      
      const response = `🎯 *Font Style:* ${data.replace(/_/g, ' ').toUpperCase()}
      
📥 *Original Text:*
\`${userText}\`

📤 *Converted Text:*
\`${convertedText}\`

✨ *Copy and use anywhere!*`;

      await editMessage(chatId, messageId, response, "Markdown", {
        inline_keyboard: fontButtons
      });
      return new Response('OK');
    }
  }
  
  return new Response('OK');
}

// Cloudflare Worker entry point
export default {
  async fetch(request, env, ctx) {
    if (request.method === 'POST') {
      try {
        const update = await request.json();
        return await handleUpdate(update);
      } catch (error) {
        console.error('Error handling request:', error);
        return new Response('Error', { status: 500 });
      }
    }
    
    return new Response('🤖 Font Changer Bot is running!');
  }
};

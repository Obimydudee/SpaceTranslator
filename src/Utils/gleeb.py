from typing import Callable

cipher:Callable[[str], str] = lambda s: s.lower().translate(str.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "⏃⏚☊⎅⟒⎎☌⊑⟟⟊☍⌰⋔⋏⍜⌿⍾⍀⌇⏁⎍⎐⍙⌖⊬⋉"
))

decipher:Callable[[str], str] = lambda s: s.translate(str.maketrans(
    "⏃⏚☊⎅⟒⎎☌⊑⟟⟊☍⌰⋔⋏⍜⌿⍾⍀⌇⏁⎍⎐⍙⌖⊬⋉",
    "abcdefghijklmnopqrstuvwxyz"
))
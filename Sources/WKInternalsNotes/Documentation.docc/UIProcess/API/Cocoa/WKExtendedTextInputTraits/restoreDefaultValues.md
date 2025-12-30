# ``WKInternalsNotes/WKExtendedTextInputTraits/restoreDefaultValues()``

拡張テキスト入力 traits を既定値へ戻す。

## Objective-C Declaration
```objective-c
- (void)restoreDefaultValues;
```

## Discussion
`typingAdaptationEnabled` や `autocapitalizationType` などを既定値に戻し、`textContentType` / `passwordRules` / 選択色を `nil` にリセットする。

## References
- [`WKExtendedTextInputTraits.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L69)
- [`WKExtendedTextInputTraits.mm#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

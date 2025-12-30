# ``WKInternalsNotes/WKExtendedTextInputTraits/autocapitalizationType``

自動大文字化の種類を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) UITextAutocapitalizationType autocapitalizationType;
```

## Default Value
初期値は `UITextAutocapitalizationTypeSentences`。

## Discussion
`init` で `UITextAutocapitalizationTypeSentences` を設定し、`restoreDefaultValues` でも同値に戻す。

## References
- [`WKExtendedTextInputTraits.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L39)
- [`WKExtendedTextInputTraits.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L49)
- [`WKExtendedTextInputTraits.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

# ``WKInternalsNotes/WKExtendedTextInputTraits/passwordRules``

`passwordRules` を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) UITextInputPasswordRules *passwordRules;
```

## Default Value
初期値は `nil`。

## Discussion
setter は `rules` をコピーして保持し、getter はコピーを返す。`restoreDefaultValues` で `nil` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L54)
- [`WKExtendedTextInputTraits.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L55)
- [`WKExtendedTextInputTraits.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

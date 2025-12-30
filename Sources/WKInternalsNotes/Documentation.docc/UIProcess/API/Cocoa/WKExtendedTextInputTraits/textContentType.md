# ``WKInternalsNotes/WKExtendedTextInputTraits/textContentType``

`textContentType` を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) UITextContentType textContentType;
```

## Default Value
初期値は `nil`。

## Discussion
setter は `type` をコピーして保持し、getter はコピーを返す。`restoreDefaultValues` で `nil` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L53)
- [`WKExtendedTextInputTraits.mm#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L65)
- [`WKExtendedTextInputTraits.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L145)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

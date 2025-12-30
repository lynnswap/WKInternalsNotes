# ``WKInternalsNotes/WKExtendedTextInputTraits/singleLineDocument``

単一行ドキュメントかどうかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isSingleLineDocument) BOOL singleLineDocument;
```

## Default Value
初期値は `NO`。

## Discussion
`restoreDefaultValues` で `NO` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L51)
- [`WKExtendedTextInputTraits.mm#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L144)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

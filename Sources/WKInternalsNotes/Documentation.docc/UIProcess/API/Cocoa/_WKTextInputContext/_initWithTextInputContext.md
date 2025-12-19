# ``WKInternalsNotes/_WKTextInputContext/_initWithTextInputContext(_:)``

WebCore の `ElementContext` から初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithTextInputContext:(const WebCore::ElementContext&)context;
```

## Discussion
`context` を `_textInputContext` に保存して返す。

## References
- [`_WKTextInputContextInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextInputContextInternal.h#L34)
- [`_WKTextInputContext.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextInputContext.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

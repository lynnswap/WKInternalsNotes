# ``WKInternalsNotes/WKTextPlaceholder/elementContext``

保持している要素コンテキストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) const WebCore::ElementContext& elementContext;
```

## Default Value
作成時に設定される。

## Discussion
`initWithElementContext:` で保持した `_elementContext` をそのまま返す。

## References
- [`WKTextPlaceholder.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextPlaceholder.h#L44)
- [`WKTextPlaceholder.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextPlaceholder.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

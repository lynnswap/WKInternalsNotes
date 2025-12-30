# ``WKInternalsNotes/WKTextPlaceholder/initWithElementContext(_:)``

要素コンテキストを保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithElementContext:(const WebCore::ElementContext&)context;
```

## Discussion
`[self init]` で初期化した後、`_elementContext` を保持して返す。

## References
- [`WKTextPlaceholder.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextPlaceholder.h#L42)
- [`WKTextPlaceholder.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextPlaceholder.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

# ``WKInternalsNotes/WKContentWorld/_userContentWorld``

WKContentWorld をラップする _WKUserContentWorld を生成して返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, readonly) _WKUserContentWorld *_userContentWorld;
```

## Default Value
`[_WKUserContentWorld alloc] _initWithContentWorld:self` で生成したインスタンス。

## Discussion
`ALLOW_DEPRECATED_DECLARATIONS_BEGIN/END` で囲みつつ、`_WKUserContentWorld` を生成して `adoptNS(...).autorelease()` で返す。アクセスのたびに新規作成される。

## References
- [`WKContentWorldPrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorldPrivate.h#L37)
- [`WKContentWorld.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L95)
- [`_WKUserContentWorldInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentWorldInternal.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

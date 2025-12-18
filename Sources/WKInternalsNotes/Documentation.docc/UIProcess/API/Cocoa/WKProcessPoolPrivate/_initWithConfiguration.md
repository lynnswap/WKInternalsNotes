# ``WKInternalsNotes/WKProcessPool/_initWithConfiguration(_:)``

指定の `_WKProcessPoolConfiguration` で初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithConfiguration:(_WKProcessPoolConfiguration *)configuration __attribute__((objc_method_family(init))) NS_DESIGNATED_INITIALIZER;
```

## Discussion
`[super init]` 成功後に `API::Object::constructInWrapper<WebKit::WebProcessPool>` を呼び、`configuration->_processPoolConfiguration` を使って `WebProcessPool` を構築する。

## References
- [`WKProcessPoolPrivate.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L74)
- [`WKProcessPool.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

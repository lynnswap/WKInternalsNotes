# ``WKInternalsNotes/WKProcessPool/_configuration``

プロセスプールの設定を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKProcessPoolConfiguration *_configuration;
```

## Default Value
`_processPool->configuration().copy()` を `wrapper(...)` で包んだ値。

## Discussion
WebKit::WebProcessPool の設定をコピーし、`_WKProcessPoolConfiguration` の wrapper を autorelease で返す。

## References
- [`WKProcessPoolPrivate.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L84)
- [`WKProcessPool.mm#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L170)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

# ``WKInternalsNotes/WKProcessPool/_sharedProcessPool()``

共有 `WKProcessPool` インスタンスを返す。

## Objective-C Declaration
```objective-c
+ (WKProcessPool *)_sharedProcessPool;
```

## Discussion
`dispatch_once` で `WKProcessPool` を生成して `sharedProcessPool()` に保持し、以降は同じインスタンスを返す。

## References
- [`WKProcessPoolPrivate.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L80)
- [`WKProcessPool.mm#L196`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L196)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

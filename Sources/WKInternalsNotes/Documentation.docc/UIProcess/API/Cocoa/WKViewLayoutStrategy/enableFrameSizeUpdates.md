# ``WKInternalsNotes/WKViewLayoutStrategy/enableFrameSizeUpdates()``

フレームサイズ更新の有効化を要求する。

## Objective-C Declaration
```objective-c
- (void)enableFrameSizeUpdates;
```

## Discussion
基底実装は no-op で、デフォルトでは何もしない。

## References
- [`WKViewLayoutStrategy.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L110)
- [`WKViewLayoutStrategy.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

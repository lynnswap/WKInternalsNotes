# ``WKInternalsNotes/WKViewLayoutStrategy/disableFrameSizeUpdates()``

フレームサイズ更新の無効化を要求する。

## Objective-C Declaration
```objective-c
- (void)disableFrameSizeUpdates;
```

## Discussion
基底実装は no-op で、デフォルトでは何もしない。

## References
- [`WKViewLayoutStrategy.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L106)
- [`WKViewLayoutStrategy.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

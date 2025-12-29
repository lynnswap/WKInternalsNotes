# ``WKInternalsNotes/WKViewLayoutStrategy/frameSizeUpdatesDisabled()``

フレームサイズ更新が無効かどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)frameSizeUpdatesDisabled;
```

## Discussion
基底実装は常に `NO` を返す。

## References
- [`WKViewLayoutStrategy.mm#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L114)
- [`WKViewLayoutStrategy.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

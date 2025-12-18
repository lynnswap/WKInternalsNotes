# ``WKInternalsNotes/WKView/frameSizeUpdatesDisabled()``

フレームサイズ更新が無効かを返す。

## Objective-C Declaration
```objective-c
- (BOOL)frameSizeUpdatesDisabled;
```

## Discussion
WKView では `NO` を返す。

## References
- [`WKViewPrivate.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L56)
- [`WKView.mm#L1038`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1038)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

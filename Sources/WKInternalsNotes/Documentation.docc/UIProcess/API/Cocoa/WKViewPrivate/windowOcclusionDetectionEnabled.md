# ``WKInternalsNotes/WKView/windowOcclusionDetectionEnabled()``

ウィンドウ遮蔽検出が有効か返す。

## Objective-C Declaration
```objective-c
- (BOOL)windowOcclusionDetectionEnabled;
```

## Discussion
WKView では `NO` を返す。

## References
- [`WKViewPrivate.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L100)
- [`WKView.mm#L1133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1133)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

# ``WKInternalsNotes/_WKThumbnailView/initWithFrame(_:fromWKView:)``

WKView を元にサムネイル表示を初期化する（旧 API）。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(NSRect)frame fromWKView:(WKView *)wkView;
```

## Discussion
`initWithFrame:` で初期化したあと `WKView` を保持し、`pageRef` から `WebPageProxy` を取得する。元の `mayStartMediaWhenInWindow` と、元ビューがウィンドウ内かどうかを記録する。

## References
- [`_WKThumbnailView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L40)
- [`_WKThumbnailView.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L83)
- [`_WKThumbnailView.mm#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L88)
- [`_WKThumbnailView.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L90)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |

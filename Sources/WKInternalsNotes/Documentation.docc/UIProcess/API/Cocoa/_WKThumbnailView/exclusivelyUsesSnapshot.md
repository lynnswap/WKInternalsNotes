# ``WKInternalsNotes/_WKThumbnailView/exclusivelyUsesSnapshot``

スナップショット専用表示にするかどうかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL exclusivelyUsesSnapshot;
```

## Default Value
初期値は `NO`。

## Discussion
`NO` の場合は `_viewWasParented` / `_viewWasUnparented` で元の `WKView` / `WKWebView` にサムネイルを関連付け、イベント抑制や `mayStartMediaWhenInWindow` の調整を行う。`YES` の場合はその関連付けを行わず、スナップショットのみを表示する。

## References
- [`_WKThumbnailView.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L47)
- [`_WKThumbnailView.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L187)
- [`_WKThumbnailView.mm#L216`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L216)
- [`_WKThumbnailView.mm#L221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L221)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |

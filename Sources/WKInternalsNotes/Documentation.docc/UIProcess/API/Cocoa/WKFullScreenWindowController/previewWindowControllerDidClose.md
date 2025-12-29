# ``WKInternalsNotes/WKFullScreenWindowController/previewWindowControllerDidClose(_:)``

QuickLook プレビューが閉じられた際にフルスクリーン退出を要求する。

## Objective-C Declaration
```objective-c
- (void)previewWindowControllerDidClose:(id)previewWindowController;
```

## Discussion
通知元が現在の `_previewWindowController` と一致する場合のみ `requestExitFullScreen` を呼び、その他のインスタンスからの通知は無視する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L2276`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2276)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

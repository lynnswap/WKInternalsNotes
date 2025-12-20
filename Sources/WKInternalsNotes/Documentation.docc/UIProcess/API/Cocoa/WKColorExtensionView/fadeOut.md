# ``WKInternalsNotes/WKColorExtensionView/fadeOut()``

フェードアウトして非表示にする。

## Objective-C Declaration
```objective-c
- (void)fadeOut;
```

## Discussion
`_updateColor:visible:` を `clearColor` と `visible:NO` で呼び出す。表示中であれば `colorExtensionViewWillDisappear:` を通知し、背景色のアニメーション完了後に `hidden` が `YES` になる。

## References
- [`WKColorExtensionView.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.h#L48)
- [`WKColorExtensionView.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L58)
- [`WKColorExtensionView.mm#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L60)
- [`WKColorExtensionView.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L72)
- [`WKColorExtensionView.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L102)
- [`WKColorExtensionView.mm#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L107)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |

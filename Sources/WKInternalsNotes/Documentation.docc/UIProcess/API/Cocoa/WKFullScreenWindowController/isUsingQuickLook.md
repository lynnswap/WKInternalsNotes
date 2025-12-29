# ``WKInternalsNotes/WKFullScreenWindowController/isUsingQuickLook``

QuickLook を使ったフルスクリーン表示かどうかを返す。

## Objective-C Declaration
```objective-c
@property (readonly, assign, nonatomic) BOOL isUsingQuickLook;
```

## Default Value
初期値は `NO`。QuickLook 経路に入った場合のみ `YES` になる。

## Discussion
アクセサは `_isUsingQuickLook` を返す。`_enterFullScreen` で `manager->isImageElement()` と entitlement を満たすと `YES` に設定される。

## References
- [`WKFullScreenWindowControllerIOS.mm#L920`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L920)
- [`WKFullScreenWindowControllerIOS.mm#L1028`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1028)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

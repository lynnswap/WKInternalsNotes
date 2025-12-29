# ``WKInternalsNotes/WKFullScreenWindowController/imageDimensions``

QuickLook フルスクリーン表示時の画像サイズを保持する。

## Objective-C Declaration
```objective-c
@property (readonly, assign, nonatomic) CGSize imageDimensions;
```

## Default Value
初期値は `CGSizeZero`。QuickLook 経路でフルスクリーンに入る際に `mediaDimensions` が設定される。

## Discussion
アクセサは `_imageDimensions` を返す。`_enterFullScreen` の QuickLook 分岐で `manager->isImageElement()` が成立した場合に `mediaDimensions` が保存される。

## References
- [`WKFullScreenWindowControllerIOS.mm#L925`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L925)
- [`WKFullScreenWindowControllerIOS.mm#L1031`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1031)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

# ``WKInternalsNotes/WKFullScreenViewController/pictureInPictureActive``

ピクチャ・イン・ピクチャ（PiP）のアクティブ状態を表す。

## Objective-C Declaration
```objective-c
@property (assign, nonatomic, getter=isPictureInPictureActive) BOOL pictureInPictureActive;
```

## Default Value
初期値は `NO`。

## Discussion
setter は `_pictureInPictureActive` を更新し、PiP ボタンの選択状態を変更する。

## References
- [`WKFullScreenViewController.mm#L695`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L695)
- [`WKFullScreenViewController.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

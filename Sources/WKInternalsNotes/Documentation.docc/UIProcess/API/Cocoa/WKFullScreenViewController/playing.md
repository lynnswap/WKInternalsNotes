# ``WKInternalsNotes/WKFullScreenViewController/playing``

再生中かどうかを表す。

## Objective-C Declaration
```objective-c
@property (assign, nonatomic, getter=isPlaying) BOOL playing;
```

## Default Value
初期値は `NO`。

## Discussion
setter は `_playing` を更新し、ビューが読み込まれていれば再生停止時に `showUI`、再生開始時に `autoHideDelay` で `hideUI` を予約する。

## References
- [`WKFullScreenViewController.mm#L675`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L675)
- [`WKFullScreenViewController.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

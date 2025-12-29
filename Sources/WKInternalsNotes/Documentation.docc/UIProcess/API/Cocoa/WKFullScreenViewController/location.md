# ``WKInternalsNotes/WKFullScreenViewController/location``

フルスクリーン警告表示に使うロケーション文字列を設定/取得する。

## Objective-C Declaration
```objective-c
@property (copy, nonatomic) NSString *location;
```

## Default Value
初期値は空文字列。

## Discussion
getter は `_location` を `NSString` 化して返す。`ENABLE(FULLSCREEN_DISMISSAL_GESTURES)` の場合、setter はバナー文言を更新する。

## References
- [`WKFullScreenViewController.mm#L723`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L723)
- [`WKFullScreenViewController.mm#L728`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L728)
- [`WKFullScreenViewController.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

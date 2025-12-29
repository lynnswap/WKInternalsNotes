# ``WKInternalsNotes/WKFullScreenViewController/prefersStatusBarHidden``

ステータスバーの非表示を希望するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (assign, nonatomic) BOOL prefersStatusBarHidden;
```

## Default Value
初期値は `NO`。

## Discussion
setter は `_prefersStatusBarHidden` を更新し、ステータスバーの更新とフルスクリーンインセット更新を行う。getter は `_animating` または `_prefersStatusBarHidden` が `true` の場合に `YES` を返す。

## References
- [`WKFullScreenViewController.mm#L658`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L658)
- [`WKFullScreenViewController.mm#L975`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L975)
- [`WKFullScreenViewController.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

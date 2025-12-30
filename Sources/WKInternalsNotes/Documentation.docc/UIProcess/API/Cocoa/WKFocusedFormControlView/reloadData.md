# ``WKInternalsNotes/WKFocusedFormControlView/reloadData(_:)``

delegate から状態を取得して表示を更新する。

## Objective-C Declaration
```objective-c
- (void)reloadData:(BOOL)animated;
```

## Discussion
前後の矩形・現在の矩形、`submitActionName`、`hasNextNode`/`hasPreviousNode` を delegate から取得して更新し、マスク位置をリセットして保留中のフォーカス要求をクリアする。

## References
- [`WKFocusedFormControlView.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L58)
- [`WKFocusedFormControlView.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

# ``WKInternalsNotes/WKContentView/_elementDidBlur()``

フォーカスが外れた際の入力状態をクリーンアップする。

## Objective-C Declaration
```objective-c
- (void)_elementDidBlur;
```

## Discussion
入力セッションや補助ビューを終了し、フォーカス情報や編集状態のフラグを初期化する。必要に応じてキーボードの非表示や UI 更新を行う。

## References
- [`WKContentViewInteraction.h#L812`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L812)
- [`WKContentViewInteraction.mm#L8620`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8620)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

# ``WKInternalsNotes/WKContentView/_selectionChanged()``

選択状態変更時の内部処理を行う。

## Objective-C Declaration
```objective-c
- (void)_selectionChanged;
```

## Discussion
選択補正フラグとキャッシュを更新し、必要に応じて選択更新を即時実行する。候補ビュー更新が必要な場合は入力デリゲートへ通知し、最後に `WKWebView` へエディタ状態変更を通知する。

## References
- [`WKContentViewInteraction.h#L817`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L817)
- [`WKContentViewInteraction.mm#L9326`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9326)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

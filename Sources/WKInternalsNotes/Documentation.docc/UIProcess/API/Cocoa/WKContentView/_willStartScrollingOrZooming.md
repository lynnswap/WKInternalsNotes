# ``WKInternalsNotes/WKContentView/_willStartScrollingOrZooming()``

スクロール/ズーム開始時の内部処理を行う。

## Objective-C Declaration
```objective-c
- (void)_willStartScrollingOrZooming;
```

## Discussion
`_textInteractionWrapper` に開始通知を送り、`WebPageProxy` の `isScrollingOrZooming` を `true` にする。Pepper UI Core 環境ではフォーカス移動ナビゲーションを解除する。

## References
- [`WKContentViewInteraction.h#L823`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L823)
- [`WKContentViewInteraction.mm#L4158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4158)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

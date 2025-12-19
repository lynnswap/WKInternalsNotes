# ``WKInternalsNotes/WKContentView/_willBeginTextInteractionInTextInputContext(_:)``

テキストインタラクション開始時の前処理を行う。

## Objective-C Declaration
```objective-c
- (void)_willBeginTextInteractionInTextInputContext:(_WKTextInputContext *)context;
```

## Discussion
プレースホルダ表示を抑制し、アクティブなテキストインタラクション数を増やす。初回の開始では選択表示の抑制とフラグ更新を行う。

## References
- [`WKContentViewInteraction.h#L918`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L918)
- [`WKContentViewInteraction.mm#L7504`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7504)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

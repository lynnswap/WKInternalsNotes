# ``WKInternalsNotes/WKContentView/_didFinishTextInteractionInTextInputContext(_:)``

テキストインタラクション終了時の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didFinishTextInteractionInTextInputContext:(_WKTextInputContext *)context;
```

## Discussion
プレースホルダ表示を戻し、アクティブ数を減らす。最後のインタラクション終了時に必要ならフォーカス要素の再表示を遅延させ、選択表示の復帰を許可する。

## References
- [`WKContentViewInteraction.h#L919`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L919)
- [`WKContentViewInteraction.mm#L7520`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7520)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

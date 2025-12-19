# ``WKInternalsNotes/WKContentView/makeTextSelectionViewsNonInteractiveForScope()``

テキスト選択ビューを一時的に非インタラクティブにする。

## Objective-C Declaration
```objective-c
- (ScopeExit<Function<void()>>)makeTextSelectionViewsNonInteractiveForScope;
```

## Discussion
`managedTextSelectionViews` とその子孫で `userInteractionEnabled` のものを収集して無効化し、スコープ終了時に元へ戻す `ScopeExit` を返す。

## References
- [`WKContentViewInteraction.h#L1008`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1008)
- [`WKContentViewInteraction.mm#L1218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1218)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

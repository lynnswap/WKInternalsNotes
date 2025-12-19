# ``WKInternalsNotes/WKContentView/setGrammarCheckingEnabled(_:)``

文法チェックの有効/無効を設定する。

## Objective-C Declaration
```objective-c
- (void)setGrammarCheckingEnabled:(BOOL)enabled;
```

## Discussion
現在の状態と同じ場合は何もしない。変更が必要な場合は `TextChecker` を更新し、Web プロセスへ反映する。

## References
- [`WKContentViewInteraction.h#L949`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L949)
- [`WKContentViewInteraction.mm#L12163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

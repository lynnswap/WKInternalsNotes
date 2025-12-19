# ``WKInternalsNotes/WKContentView/setContinuousSpellCheckingEnabled(_:)``

連続スペルチェックの有効/無効を設定する。

## Objective-C Declaration
```objective-c
- (void)setContinuousSpellCheckingEnabled:(BOOL)enabled;
```

## Discussion
`TextChecker` の設定を更新し、変更があった場合は Web プロセスへ反映する。

## References
- [`WKContentViewInteraction.h#L948`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L948)
- [`WKContentViewInteraction.mm#L12157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12157)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

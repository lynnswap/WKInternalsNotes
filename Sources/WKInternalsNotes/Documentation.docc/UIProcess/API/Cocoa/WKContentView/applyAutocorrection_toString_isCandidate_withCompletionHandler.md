# ``WKInternalsNotes/WKContentView/applyAutocorrection(_:toString:isCandidate:withCompletionHandler:)``

オートコレクションを適用し、結果の矩形を返す。

## Objective-C Declaration
```objective-c
- (void)applyAutocorrection:(NSString *)correction toString:(NSString *)input isCandidate:(BOOL)isCandidate withCompletionHandler:(void (^)(UIWKAutocorrectionRects *rectsForCorrection))completionHandler;
```

## Discussion
内部置換処理を実行し、適用できた場合は補正後の先頭/末尾矩形を `UIWKAutocorrectionRects` として返す。

## References
- [`WKContentViewInteraction.h#L923`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L923)
- [`WKContentViewInteraction.mm#L5966`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5966)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

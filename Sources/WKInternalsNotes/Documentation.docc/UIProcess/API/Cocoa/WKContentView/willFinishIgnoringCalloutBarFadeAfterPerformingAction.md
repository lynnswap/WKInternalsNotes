# ``WKInternalsNotes/WKContentView/willFinishIgnoringCalloutBarFadeAfterPerformingAction()``

選択コマンドのフェード抑制を解除する準備をする。

## Objective-C Declaration
```objective-c
- (void)willFinishIgnoringCalloutBarFadeAfterPerformingAction;
```

## Discussion
`_ignoreSelectionCommandFadeCount` を増やして editor state 更新を依頼し、次の描画更新後にカウントを戻す。

## References
- [`WKContentViewInteraction.h#L860`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L860)
- [`WKContentViewInteraction.mm#L6405`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6405)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

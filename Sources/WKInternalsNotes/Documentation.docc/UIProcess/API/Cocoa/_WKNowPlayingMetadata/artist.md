# ``WKInternalsNotes/_WKNowPlayingMetadata/artist``

Now Playing のアーティスト名を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *artist;
```

## Default Value
生成直後は `nil`。`_setNowPlayingMetadataObserver` が発火すると `metadata.artist` をコピーして設定する。

## Discussion
テスト用の Now Playing メタデータ観測で `WebCore::NowPlayingMetadata` の `artist` を `NSString` に変換し、`setArtist:` で代入して observer に渡す。`copy` 属性のため渡された文字列をコピー保持する。

## References
- [`WKWebViewPrivateForTesting.h#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L236)
- [`WKWebViewTesting.mm#L294`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L294)
- [`WKWebViewTesting.mm#L297`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L297)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
